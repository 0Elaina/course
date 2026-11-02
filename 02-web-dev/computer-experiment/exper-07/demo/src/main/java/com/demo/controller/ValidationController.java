package com.demo.controller;

import com.demo.entity.ValidCommodity;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;

@Controller
public class ValidationController {

    // 进入验证页面，预置默认数据（也可通过URL重置）
    @GetMapping("/valid")
    public String init(Model model) {
        if (!model.containsAttribute("com")) {
            ValidCommodity commodity = new ValidCommodity();
            commodity.setPid(1001);
            commodity.setPname("砀山梨10斤箱装大果");
            commodity.setTcode("11B");
            commodity.setPprice(19.9f);
            commodity.setStocks(14532);
            commodity.setTextadv("中国传统三大名梨之首，汁多味甜且润肺止咳而驰名中外。");
            model.addAttribute("com", commodity);
        }
        return "valid";
    }

    // 提交表单进行验证
    @PostMapping("/add")
    public String addCommodity(@ModelAttribute("com") @Validated ValidCommodity commodity,
                               BindingResult bindingResult) {
        if (bindingResult.hasErrors()) {
            return "valid";
        }
        return "success";
    }
}
