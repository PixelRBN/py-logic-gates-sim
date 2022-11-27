import dearpygui.dearpygui as dpg

dpg.create_context()

node_links = []


def on():
    with dpg.node(parent="node_editor"):
        with dpg.node_attribute(attribute_type=1):
            dpg.add_text("1")


def off():
    with dpg.node(parent="node_editor"):
        with dpg.node_attribute(attribute_type=1):
            dpg.add_text("0")


def and_gate():
    with dpg.node(label="AND", parent="node_editor", tag="and"):
        with dpg.node_attribute(attribute_type=0):
            dpg.add_text(default_value="0", tag="and_1")

        with dpg.node_attribute(attribute_type=0):
            dpg.add_text(default_value="0", tag="and_2")

        with dpg.node_attribute(attribute_type=1):
            dpg.add_text(default_value="0", tag="and_out")


def update():
    for i in node_links:
        node_attribute_requester = dpg.get_item_parent(i[0])
        node_attribute_sender = -1

        for link in dpg.get_item_children("node_editor", 0):
            # attr_1 is output, attr_2 is input
            attr_1, attr_2 = dpg.get_item_configuration(link)['attr_1'], dpg.get_item_configuration(link)['attr_2']
            if node_attribute_requester == attr_2:
                node_attribute_sender = attr_1
                break

        text_item = dpg.get_item_children(i[0], 1)[0]
        print(dpg.get_value(text_item))

        # Setting the vale in the input node when connected
        dpg.configure_item(dpg.get_item_children(i[1], 1)[0], default_value=dpg.get_value(text_item)[-1])

        if dpg.get_item_parent(dpg.get_item_children(i[1], 1)[0]) == "and":
            print("AND Gate")


def node_gui():

    def link_callback(sender, app_data):

        # app_data -> (link_id1, link_id2)
        dpg.add_node_link(app_data[0], app_data[1], parent=sender)
        node_links.append(app_data)
        update()

    def delink_callback(sender, app_data):
        dpg.delete_item(app_data)
        node_links.remove(
            (dpg.get_item_configuration(app_data)["attr_1"], dpg.get_item_configuration(app_data)["attr_2"]))
        dpg.delete_item(app_data)

    with dpg.window(label="Node Editor", width=920, height=700, pos=(250, 0), no_move=True, no_collapse=True):

        with dpg.node_editor(tag="node_editor", callback=link_callback, delink_callback=delink_callback):
            pass

# TODO configure_item()
