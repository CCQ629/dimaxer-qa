import dimaxer_ui as ui

#  https://project.feishu.cn/k112k5/issue/detail/7016391397?parentUrl=%2Fk112k5%2Fissue%2Fhomepage&openScene=2
def p0_times_animation_index_1():
    """打开 vki_59_demo 模型 → 选中网格 → Color Map 选 Pressure → 展开工具条 → 依次输入 index 0~5。"""

    # 1. 导入新模型
    ui.import_model_post(r"vki_59_demo/simulations/vki_59_demo_simulation.dmx")
    ui.wait_ui_idle()

    # 2. 选中 vki59 网格
    ui.item_click("post.ribbon.mesh_select_vki59_1", 0, 8)
    ui.wait_ui_idle()

    # 3. Color Map 选 Pressure
    ui.combo_click("post.scene_properties.value_cell", "Pressure")

    # 4. 展开时间工具条（检测是否已展开）
    if not ui.alias_exists_now("post.quickaccess.forward_step"):
        ui.item_click("post.quickaccess.toolbar_expand", 0, 8)
        ui.wait_ui_idle()

    # 5. 依次输入 animation index 0 ~ 3
    for i in range(4):
        ui.item_input_value("post.quickaccess.animation_index", i)
        ui.wait_ui_idle()

    ui.capture_renderview(8, "post.quickaccess")
