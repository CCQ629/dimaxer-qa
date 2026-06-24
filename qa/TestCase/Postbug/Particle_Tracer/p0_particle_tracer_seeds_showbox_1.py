import dimaxer_ui as ui

#https://project.feishu.cn/k112k5/issue/detail/7015712131?parentUrl=%2Fk112k5%2Fissue%2Fhomepage&openScene=2

def p0_particle_tracer_seeds_showbox_1():
    """打开老模型 → Particle Tracer 面板 → Seeds 四选项遍历 → BoxPointSource → 勾选 ShowBox → Apply。"""

    # 1. 导入老模型
    ui.import_model_post(r"dmh1/19-0.000949999958.dmh.dat")

    # 2. 隐藏全部，选中网格
    ui.ribbon_hide_all_and_select_mesh()

    # 3. 打开 Particle Tracer 面板
    ui.item_click("post.top.particle_tracer_panel", 0, 8)
    ui.wait_ui_idle()

    # 4. 逐个遍历 Seeds 下拉框的四个选项
    ui.combo_click("post.particle_tracer.seeds", "BoxPointSource")
    ui.combo_click("post.particle_tracer.seeds", "CylinderPointSource")
    ui.combo_click("post.particle_tracer.seeds", "HighResLineSource")
    ui.combo_click("post.particle_tracer.seeds", "PointSource")

    # 5. 换回 BoxPointSource（此时 ShowBox 变为未勾选，需手动勾选）
    ui.combo_click("post.particle_tracer.seeds", "BoxPointSource")
    ui.wait_ui_idle()
    
    # 6. 勾选 ShowBox
    ui.item_click("post.particle_tracer.showbox", 0, 8)
    ui.wait_ui_idle()
    ui.capture_renderview(8)

    # 7. Apply
    ui.item_click_apply("post.particle_tracer.apply", 0, 8)

 
