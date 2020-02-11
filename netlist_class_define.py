import pandas as pd

class module_class():
    def __init__(self, name):
        self._module_name     = name
        #self._pin_name_frame  = pd.DataFrame(columns = ['pin_index', 'width'])
        self._pin_name_dict   = {}
        self._pin_list        = []
        self._pin_index       = 0
        self._node_dict       = {}
        self._inst_list       = []
        self._buf_list        = []
        self._inv_list        = []
        self._and_list        = []
        self._or_list         = []
        self._ff_list         = []
        self._lat_list        = []
        self._node_dict['Tielow']   = node_class_lite('Tielow',  'wire')
        self._node_dict['Tiehigh']  = node_class_lite('Tiehigh', 'wire')

    # add buf
    def add_buf(self, o_name, i_name):
        self._buf_list.append([o_name, i_name])
    # add and
    def add_and(self, o_name, i0_name, i1_name):
        self._and_list.append([o_name, i0_name, i1_name])
    # add or
    def add_or(self, o_name, i0_name, i1_name):
        self._or_list.append([o_name, i0_name, i1_name])
    # add inv
    def add_inv(self, o_name, i_name):
        self._inv_list.append([o_name, i_name])
    # add ff
    def add_ff(self, o_name, d_name, clk_name):
        self._ff_list.append([o_name, d_name, clk_name])
    # add lat
    def add_lat(self, o_name, d_name, clk_name):
        self._lat_list.append([o_name, d_name, clk_name])


    def get_buf_list(self):
        return self._buf_list
    def get_inv_list(self):
        return self._inv_list
    def get_and_list(self):
        return self._and_list
    def get_or_list(self):
        return self._or_list
    def get_ff_list(self):
        return self._ff_list
    def get_lat_list(self):
        return self._lat_list


    # add pin during module declar
    def add_pin(self, pin_name):
        self._pin_name_dict[pin_name] = 0
        self._pin_list.append(pin_name)
        #self._pin_index = self._pin_index + 1

    # set pin width in node define
    def set_pin_width(self, pin_name, pin_width):
        if pin_name in self._pin_list:
            self._pin_name_dict[pin_name] = pin_width
        else:
            self.add_pin(pin_name)
            self._pin_name_dict[pin_name] = pin_width
            #self.add_node(pin_name, 'wire')
            print('[Warning] Pin %s not in pin list of module %s'%(pin_name, self._module_name))
        
    # add node bus in node define
    def add_bus(self, node_name, node_width, node_type):
        self.set_pin_width(node_name, node_width)
        # add node lite to node dict
        while node_width >= 0:
            flat_node_name = '%s__busbit__%s__'%(node_name, node_width)
            current_node = node_class_lite(flat_node_name, node_type)
            self._node_dict[flat_node_name] = current_node
            node_width = node_width - 1

    # add single bit node in node define
    def add_node(self, node_name, node_type):
        current_node = node_class_lite(node_name, node_type)
        self._node_dict[node_name] = current_node

    # add inst lite define
    def add_instance(self, inst_name, inst):
        self._inst_list.append(inst)

#    # add connection request to node lite
#    def connection_request_bus_by_index(self, sub_inst_name, module_bus_name, inst_pin_index, start_bit, end_bit):
#        i = start_bit
#        while i <= end_bit:
#            self._node_dict['%s__busbit__%s__'%(module_bus_name, i)].bus_connection_request_by_index(sub_inst_name,
#                                                                                                     inst_pin_index, i)
#            #print('[Info] Connection defined for %s__busbit__%s__ to node inst[%s]index[%s]bit[%s]'%(module_bus_name, i, sub_inst_name, inst_pin_index, i))
#            i = i + 1
#        return

    # add connection request to node lite
    def connection_request_pin_by_index(self, sub_inst_name, module_pin_name, inst_pin_index, bus_index):
        self._node_dict[module_pin_name].pin_connection_request_by_index(sub_inst_name, inst_pin_index, bus_index)
        #print('[Info] Connection defined for %s to node inst[%s]index[%s]'%(module_pin_name, sub_inst_name, inst_pin_index))
        return

    # add connection request to node lite
    def connection_request_pin_by_name(self, sub_inst_name, module_pin_name, inst_pin_name):
        if not module_pin_name in self._node_dict.keys():
            self.add_node(module_pin_name, 'wire')
        self._node_dict[module_pin_name].pin_connection_request_by_index(sub_inst_name, inst_pin_name, -1)
        #print('[Info] Connection defined for %s to node inst[%s]name[%s]'%(module_pin_name, sub_inst_name, inst_pin_name))
        return

    def get_node_dict(self):
        return self._node_dict

    def get_name(self):
        return self._module_name

    def get_inst_list(self):
        return self._inst_list

    def get_pin_name_by_index(self, pin_index):
        #print(self._pin_name_frame[self._pin_name_frame.pin_index == pin_index].index.values[0])
        #return self._pin_name_frame[self._pin_name_frame.pin_index == pin_index].index.values[0]
        return self._pin_list[pin_index]

    def get_bus_width(self, name):
        if name in set(self._pin_list):
            return self._pin_name_dict[name]
        else:
            self.add_pin(name)
            self.add_node(name, 'wire')
            #print('[Warning] Pin %s not in pin list of module %s while get'%(name, self._module_name))
            return self._pin_name_dict[name]

# lite insance class during compiling, not for elab
class instance_class_lite():
    def __init__(self, ref_name, name):
        self._ref_name        = ref_name
        self._instance_name   = name

    def get_name(self):
        return self._instance_name

    def get_ref_name(self):
        return self._ref_name

# instance full class during elab
class instance_class():
    def __init__(self, ref_name, name, path_name, father_inst):
        self._ref_name        = ref_name
        self._instance_name   = name
        self._father_inst     = father_inst
        self._sub_inst_dict   = {}
        self._node_dict       = {}

    def add_node(self, node_name, node_lite):
        current_node = node_class(node_name, node_lite.get_type(), node_lite.get_connection_map(), self)
        self._node_dict[node_name] = current_node
        return current_node

    def add_child(self, name, child_inst):
        self._sub_inst_dict[name] = child_inst

    def get_name(self):
        return self._instance_name

    def get_child(self, name):
        return self._sub_inst_dict[name]

    def get_sub_inst_dict(self):
        return self._sub_inst_dict

    def get_ref_name(self):
        return self._ref_name

    def get_node(self, node_name):
        return self._node_dict[node_name]

    def get_node_dict(self):
        return self._node_dict

# lite node class for compiling, not elab
class node_class_lite():
    def __init__(self, name, node_type):
        self._node_name       = name
        self._node_type       = node_type
        self._connection_map  = []

    def pin_connection_request_by_index(self, sub_inst_name, inst_pin_index, bus_index):
        self._connection_map.append([sub_inst_name, inst_pin_index, bus_index])

#    def bus_connection_request_by_index(self, sub_inst_name, inst_pin_index, bit):
#        self._connection_map.append([sub_inst_name, inst_pin_index, bit])

    def get_type(self):
        return self._node_type

    def get_connection_map(self):
        return self._connection_map

# node full class, for elab
class node_class():
    def __init__(self, name, node_type, connection_map, inst):
        self._node_name                 = name
        self._inst                      = inst
        #self._value                     = None
        self._node_type                 = node_type
        self._connection_map            = connection_map
        self._driver                    = signal_class('Z')
        self._loader                    = signal_class('Z')
        self._logical_driver_list       = []
        self._logical_loading_list      = []
        self._physical_driver_list      = []
        self._physical_loading_list     = []
        self._blocked                   = False
        #self._equal_right_list          = []
        #self._active_cnt                = 0
        if self._node_name == 'Tiehigh':
            self._driver = signal_class('H')
            self._blocked = True
        elif self._node_name == 'Tielow':
            self._driver = signal_class('L')
            self._blocked = True

    def calc(self, node):
        return

    def add_logical_loading(self, node):
        self._logical_loading_list.append(node)

    def add_logical_driver(self, node):
        self._logical_driver_list.append(node)

    def add_physical_loading(self, node):
        self._physical_loading_list.append(node)

    def add_physical_driver(self, node):
        self._physical_driver_list.append(node)

    def get_logical_loading_list(self):
        return self._logical_loading_list

    def get_logical_driver_list(self):
        return self._logical_driver_list

    def get_physical_loading_list(self):
        return self._physical_loading_list

    def get_physical_driver_list(self):
        return self._physical_driver_list

    def set_block(self, blocked):
        if blocked:
            self._blocked = True
        else:
            self._blocked = False
#    def add_equal_right(self, right_list):
#        self._equal_right_list = right_list

    def get_name(self):
        return self._node_name

    def get_full_name(self):
        return '%s/%s'%(self._inst.get_name(), self._node_name)

    def get_type(self):
        return self._node_type

    def get_connection_map(self):
        return self._connection_map

    def get_value(self):
        return self._driver

    def connect(self, target_node):
        #print('[Info] Connection between %s and %s'%(self.get_full_name(), target_node.get_full_name()))
        # both inout
        if self._node_type == 'inout' and target_node.get_type() == 'inout':
            self.add_physical_loading(target_node)
            target_node.add_physical_driver(self)
            self.add_physical_driver(target_node)
            target_node.add_physical_loading(self)
        # module input/wire/inout to inst input
        elif (self._node_type == 'input' or self._node_type == 'wire' or self._node_type == 'inout') \
        and (target_node.get_type() == 'input' or target_node.get_type() == 'inout'):
            self.add_physical_loading(target_node)
            target_node.add_physical_driver(self)
        # inst output to module output/wire/inout
        elif (self._node_type == 'output' or self._node_type == 'wire' or self._node_type == 'inout') \
        and (target_node.get_type() == 'output' or target_node.get_type() == 'inout'):
            self.add_physical_driver(target_node)
            target_node.add_physical_loading(self)

    def set_node_value(self, signal):
        result = signal_class(signal, None)
        if self._driver.get_value() == 'H' and signal == 'L':
            result.set_edge('F')
        elif self._driver.get_value() == 'L' and signal == 'H':
            result.set_edge('R')
        elif (self._driver.get_value() == 'Z' or self._driver.get_value() == 'X') and \
             (signal == 'L' or signal == 'H'):
            result.set_edge('I')
        #print('force %s'%result.get_value())
        self._driver = result
        #print('force %s'%self._driver.get_value())


    def calc_value_self(self):
        #print(self._loader)
        if len(self._physical_driver_list) > 1:
            print('[Warning] Mult-drive on node %s'%self._node_name)
        # get right value from physical driver for this node
        temp_signal = signal_class('Z', None)
        for driver_node in self._physical_driver_list:
            #print('%s'%self.get_name())
            #print('%s'%driver_node.get_name())
            temp_signal = temp_signal.sum(driver_node.get_value())
        self._loader = temp_signal
        # get right value from logical driver for this node
        #print(self.get_type())
        #print(self._loader)
        #print(self.calc(self))
        if self._logical_driver_list:
            #print(self._node_name)
            #print(self.calc(self).get_value())
            self._loader = self.calc(self)
            if self._physical_driver_list:
                print('[Warning] Mult-drive on node %s'%self._node_name)
        # push value to self driver
        if not self._blocked:
            self._driver = self._loader
        #print(self._driver.get_value())

    def calc_value_push(self):
        # push observe wave to loading
        for loading_node in self._physical_loading_list + self._logical_loading_list:
            loading_node.calc_value_self()
            if loading_node.get_value().get_edge():
                loading_node.calc_value_push()

class signal_class():
    def __init__(self, value = 'Z', edge = None):
        self._value           = value
        self._edge            = edge

    def set_value(self, value):
        self._value = value

    def set_edge(self, value):
        self._edge = value

    def get_value(self):
        return self._value

    def get_edge(self):
        return self._edge

    def sum(self, new):
        result = signal_class()
        if self._value == new.get_value():
            result.set_value(self._value)
            result.set_edge(self._edge)
            return result
        elif self._value == 'X' or new.get_value() == 'X':
            result.set_value('X')
            result.set_edge(None)
            return result
        elif self._value == 'Z':
            result.set_value(new.get_value())
            result.set_edge(new.get_edge())
            return result
        elif new.get_value() == 'Z':
            result.set_value(self._value)
            result.set_edge(self._edge)
            return result

    def __and__(self, new):
        result = signal_class()
        if self._value == new.get_value():
            result.set_value(self._value)
        elif self._value == 'X' or new.get_value() == 'X':
            result.set_value('X')
        elif self._value == 'Z' or new.get_value() == 'Z':
            result.set_value('X')
        else:
            result.set_value('L')

        if self._edge == new.get_edge():
            result.set_edge(self._edge)
        elif (self._edge == 'R' and new.get_edge() == 'F') or (self._edge == 'F' and new.get_edge() == 'R'):
            result.set_edge(None)
        elif ((not new.get_edge()) and new.get_value() == 'L') or (self._value == 'L' and (not self._edge)):
            result.set_edge(None)
        elif (not new.get_edge()) and new.get_value() == 'H':
            result.set_edge(self._edge)
        elif self._value == 'H' and (not self._edge):
            result.set_edge(new.get_edge())
        elif self._edge == 'I' or new.get_edge() == 'I':
            result.set_edge('I')

        return result

    def __or__(self, new):
        result = signal_class()
        if self._value == new.get_value():
            result.set_value(self._value)
        elif self._value == 'X' or new.get_value() == 'X':
            result.set_value('X')
        elif self._value == 'Z' or new.get_value() == 'Z':
            result.set_value('X')
        else:
            result.set_value('H')

        if self._edge == new.get_edge():
            result.set_edge(self._edge)
        elif (self._edge == 'R' and new.get_edge() == 'F') or (self._edge == 'F' and new.get_edge() == 'R'):
            result.set_edge(None)
        elif ((not new.get_edge()) and new.get_value() == 'H') or (self._value == 'H' and (not self._edge)):
            result.set_edge(None)
        elif (not new.get_edge()) and new.get_value() == 'L':
            result.set_edge(self._edge)
        elif self._value == 'L' and (not self._edge):
            result.set_edge(new.get_edge())
        elif self._edge == 'I' or new.get_edge() == 'I':
            result.set_edge('I')

        return result


    def __invert__(self):
        result = signal_class()
        if self._value == 'H':
            result.set_value('L')
        if self._value == 'L':
            result.set_value('H')
        else:
            result.set_value(elf._value)

        if self._edge == 'R':
            result.set_edge('F')
        if self._edge == 'F':
            result.set_edge('R')
        else:
            result.set_edge(self._edge)

        return result


# elab data class
class elab_data_class():
    def __init__(self, module_dict, black_dict, top_module_name):
        self._module_dict = module_dict
        self._black_dict  = black_dict
        self._inst_dict   = {}
        self._top_name    = top_module_name

    # instance elab before node connection
    def inst_elab(self):
        # build inst tree from top
        self.add_true_inst(self._top_name, self._top_name, '', self._module_dict[self._top_name].get_node_dict(), None)

    # connection elab after inst elab
    def connection_elab(self):
        # add connection from top
        self.add_connection_from_inst(self._inst_dict['/%s'%self._top_name])
        return

    def add_true_inst(self, ref_name, name, path_name, module_node_dict, father_inst):
        # build new inst
        current_inst = instance_class(ref_name, name, path_name, father_inst)
        # add nodes based on module dict
        for node_name in module_node_dict.keys():
            #print('module %s node name %s'%(ref_name, node_name))
            current_inst.add_node(node_name, module_node_dict[node_name])
            #print(module_node_dict[node_name].get_connection_map())
        # add inst to global inst dict
        self._inst_dict['%s/%s'%(path_name, name)] = current_inst
        # if not top
        if father_inst:
            # add current inst to father's child list
            father_inst.add_child(name, current_inst)

        # if current inst not black box, add sub inst
        if ref_name in self._module_dict.keys():
            # add sub inst in new inst
            for sub_inst in self._module_dict[ref_name].get_inst_list():
                # path name of sub inst
                sub_path_name = '%s/%s'%(path_name, name)
                # if sub inst not black box
                if sub_inst.get_ref_name() in self._module_dict.keys():
                    # add sub inst
                    self.add_true_inst(sub_inst.get_ref_name(), sub_inst.get_name(), sub_path_name,
                                       self._module_dict[sub_inst.get_ref_name()].get_node_dict(), current_inst)
                # if sub inst is black box
                else:
                    # add sub black box inst
                    self.add_true_inst(sub_inst.get_ref_name(), sub_inst.get_name(), sub_path_name,
                                       self._black_dict[sub_inst.get_ref_name()].get_node_dict(), current_inst)

    def add_connection_from_inst(self, inst):
        # connect every node based on connection map
        node_dict = inst.get_node_dict()


        if inst.get_ref_name() in self._black_dict.keys():
            return
        # add calc
        # and
        for and_connection in self._module_dict[inst.get_ref_name()].get_and_list():
            for node_name in and_connection:
                if not node_name in node_dict.keys():
                    node_dict[node_name] = node_class(node_name, 'wire', [], inst)
            o  = and_connection[0]
            i0 = and_connection[1]
            i1 = and_connection[2]
            node_dict[o].add_logical_driver(node_dict[i0])
            node_dict[o].add_logical_driver(node_dict[i1])
            node_dict[i0].add_logical_loading(node_dict[o])
            node_dict[i1].add_logical_loading(node_dict[o])
            #node_dict[o].add_equal_right([node_dict[i0], node_dict[i1]])
            node_dict[o].calc = calc_and
        # or
        for or_connection in self._module_dict[inst.get_ref_name()].get_or_list():
            for node_name in or_connection:
                if not node_name in node_dict.keys():
                    node_dict[node_name] = node_class(node_name, 'wire', [], inst)
            o  = or_connection[0]
            i0 = or_connection[1]
            i1 = or_connection[2]
            node_dict[o].add_logical_driver(node_dict[i0])
            node_dict[o].add_logical_driver(node_dict[i1])
            node_dict[i0].add_logical_loading(node_dict[o])
            node_dict[i1].add_logical_loading(node_dict[o])
            #node_dict[o].add_equal_right([node_dict[i0], node_dict[i1]])
            node_dict[o].calc = calc_or
        # buf
        for buf_connection in self._module_dict[inst.get_ref_name()].get_buf_list():
            for node_name in buf_connection:
                if not node_name in node_dict.keys():
                    node_dict[node_name] = node_class(node_name, 'wire', [], inst)
            o  = buf_connection[0]
            i0 = buf_connection[1]
            node_dict[o].add_logical_driver(node_dict[i0])
            node_dict[i0].add_logical_loading(node_dict[o])
            #node_dict[o].add_equal_right([node_dict[i0]])
            node_dict[o].calc = calc_buf
        # inv
        for inv_connection in self._module_dict[inst.get_ref_name()].get_inv_list():
            for node_name in inv_connection:
                if not node_name in node_dict.keys():
                    node_dict[node_name] = node_class(node_name, 'wire', [], inst)
            o  = inv_connection[0]
            i0 = inv_connection[1]
            node_dict[o].add_logical_driver(node_dict[i0])
            node_dict[i0].add_logical_loading(node_dict[o])
            #node_dict[o].add_equal_right([node_dict[i0]])
            node_dict[o].calc = calc_inv
        # ff
        for ff_connection in self._module_dict[inst.get_ref_name()].get_ff_list():
            for node_name in ff_connection:
                if not node_name in node_dict.keys():
                    node_dict[node_name] = node_class(node_name, 'reg', [], inst)
            q   = ff_connection[0]
            d   = ff_connection[1]
            clk = ff_connection[2]
            node_dict[q].add_logical_driver(node_dict[clk])
            node_dict[q].add_logical_driver(node_dict[d])
            node_dict[clk].add_logical_loading(node_dict[q])
            node_dict[d].add_logical_loading(node_dict[q])
            #node_dict[o].add_equal_right([node_dict[i0]])
            node_dict[q].calc = calc_ff


        # connect for every node
        for node in node_dict.values():
            # if no connection request
            if not node.get_connection_map():
                continue

            # connect from node to node
            connection_request_list = node.get_connection_map()
            #connection_request = node.get_connection_map()
            bit_char           = ''
            target_node_name   = ''
            unknown_index      = 0


            for connection_request in connection_request_list:
                # if connection with black box
                if inst.get_child(connection_request[0]).get_ref_name() in self._black_dict.keys():
                    sub_black_box = inst.get_child(connection_request[0])
                    if str(connection_request[1]).isdigit() > 0:
                        node.connect(sub_black_box.add_node('unknown_node_%s'%unknown_index, node_class_lite('unknown_node_%s'%unknown_index, 'inout')))
                        unknown_index = unknown_index + 1
                        continue

                    if len(connection_request) == 3 and connection_request[2] > 0:
                        bit_char       = '__busbit__%s__'%connection_request[2]
                    else:
                        bit_char       = ''
                    fake_node_name = connection_request[1] + bit_char
                    node.connect(sub_black_box.add_node(fake_node_name, node_class_lite(fake_node_name, 'inout')))
                    continue

                # if bus bit, add bus bit string
                if len(connection_request) == 3:
                    bit_char       = '__busbit__%s__'%connection_request[2]
    
                # if connection by index
                if str(connection_request[1]).isdigit():
                    # get name by index
                    target_node_name = self._module_dict[inst.get_child(connection_request[0]).get_ref_name()].get_pin_name_by_index(connection_request[1])
                # or by name
                else:
                    # get name in connection request
                    target_node_name = connection_request[1]
                # by index or not, target node name concat
                target_node_name = target_node_name + bit_char
                target_node = inst.get_child(connection_request[0]).get_node(target_node_name)
                # connect
                node.connect(target_node)

        # connect sub inst
        for sub_inst in inst.get_sub_inst_dict().values():
            self.add_connection_from_inst(sub_inst)

    def get_module(self, module_name):
        if module_name in self._module_dict.keys():
            return self._module_dict[module_name]
        else:
            print('[Warning] Module %s not in database'%module_name)
            #return module_class('dummy')

    def get_instance(self, instance_name):
        if instance_name in self._inst_dict.keys():
            return self._inst_dict[instance_name]
        else:
            print('[Warning] Instance %s not in database'%instance_name)
            #return instance_class('dummy', 'dummy', 'dummy')

    def force_value(self, inst_full_name, node_name, signal_value):
        inst = self.get_instance(inst_full_name)
        node = inst.get_node(node_name)
        node.set_node_value(signal_value)
        node.calc_value_push()
        node.set_block(True)
        print('[Info] Force %s at %s/%s'%(signal_value, inst_full_name, node_name))

    def release_force(self, inst_full_name, node_name):
        inst = self.get_instance(inst_full_name)
        node = inst.get_node(node_name)
        node.set_block(False)
        node.calc_value_push()
        print('[Info] Released %s/%s'%(inst_full_name, node_name))

    def pulse_clock(self, clock_list, cycle_cnt):
        for i in range(0, cycle_cnt):
            for clock in clock_list:
                inst = self.get_instance(clock[0])
                node = inst.get_node(clock[1])
                node.set_node_value('L')
                node.calc_value_push()
                node.set_node_value('H')
                node.calc_value_push()
        print('[Info] Pulsed clocks %s for %s cycles'%(clock_list, cycle_cnt))

    def observe_value(self, inst_full_name, node_name):
        inst = self.get_instance(inst_full_name)
        node = inst.get_node(node_name)
        node_full_name = node.get_full_name()
        value = node.get_value().get_value()
        print('[Info] Value of %s/%s is %s'%(inst_full_name, node.get_name(), value))
        return value

def calc_and(self_node):
    node0 = self_node.get_logical_driver_list()[0]
    node1 = self_node.get_logical_driver_list()[1]
    #self_node.set_value(node0.get_value() & node1.get_value())
    return node0.get_value() & node1.get_value()

def calc_or(self_node):
    node0 = self_node.get_logical_driver_list()[0]
    node1 = self_node.get_logical_driver_list()[1]
    #self_node.set_value(node0.get_value() | node1.get_value())
    return node0.get_value() | node1.get_value()

def calc_inv(self_node):
    node0 = self_node.get_logical_driver_list()[0]
    #self_node.set_value(node0.get_value().inv())
    #print('inv')
    return ~node0.get_value()

def calc_buf(self_node):
    node0 = self_node.get_logical_driver_list()[0]
    #self_node.set_value(node0.get_value())
    #print('buf')
    return node0.get_value()

def calc_ff(self_node):
    result = signal_class()
    clk_node = self_node.get_logical_driver_list()[0]
    d_node   = self_node.get_logical_driver_list()[1]

    if clk_node.get_value().get_edge() == 'R':
        result.set_value(d_node.get_value().get_value())

    if self_node.get_value().get_value() == 'H' and d_node.get_value().get_value() == 'L':
        result.set_edge('F')
    elif self_node.get_value().get_value() == 'L' and d_node.get_value().get_value() == 'H':
        result.set_edge('R')
    elif (self_node.get_value().get_value() == 'H' or self_node.get_value().get_value() == 'L') and \
       (d_node.get_value().get_value() == 'X' or d_node.get_value().get_value() == 'Z'):
        result.set_edge('I')
    elif (self_node.get_value().get_value() == 'X' or self_node.get_value().get_value() == 'Z') and \
       (d_node.get_value().get_value() == 'H' or d_node.get_value().get_value() == 'L'):
        result.set_edge('I')

    #print(result.get_value(), result.get_edge())
    return result
