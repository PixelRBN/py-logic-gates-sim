from node import *
import dearpygui.dearpygui as dpg


def add_gate():

    if dpg.get_value("list") == "1":
        on()
    if dpg.get_value("list") == "0":
        off()
    if dpg.get_value("list") == "AND":
        and_gate()


gates = ["1", "0", "AND", "OR", "NOT"]
dpg.create_context()

with dpg.window(label="Add Gates", height=700, width=250, no_move=True, no_collapse=True):
    dpg.add_listbox(tag="list", items=gates)
    dpg.add_button(label="Add Gate", callback=add_gate)
    dpg.add_button(label="Get", callback=update)


node_gui()


dpg.create_viewport(title='Custom Title', width=1200, height=700)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
