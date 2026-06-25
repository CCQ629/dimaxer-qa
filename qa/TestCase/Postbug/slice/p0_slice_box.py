import dimaxer_ui as ui


def slice_box():
    ui.import_model_post(r"vki_59_demo/simulations/vki_59_demo_simulation.dmx")
    ui.item_click("post.ribbon.hide_all")
    ui.wait_ui_idle()

    ui.item_click("post.ribbon.mesh_select_vki59_1")
    ui.item_click("post.ribbon.vis_vki59_1")

    ui.item_click("post.top.slice_panel")
    ui.combo_click("post.slice.combo_type", "Box")
    ui.item_click("post.slice.show_preview")
    ui.item_input_value("post.slice.length", "0.05")
    ui.item_click("post.slice.apply")
    ui.wait_ui_idle()

    ui.item_click("post.ribbon.hide_all")
    ui.item_click_scene_tree_ref_contains("VisibilityCheckbox", "_Slice1")
    ui.capture_renderview(8)
