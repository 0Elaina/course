package com.demo.controller;

import com.demo.entity.Commodity;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import java.util.ArrayList;
import java.util.List;

@Controller
public class BootstrapController {

    @GetMapping({"/bootstrap", "/goods"})
    public String showBootstrap(Model model) {
        List<Commodity> list = new ArrayList<>();
        list.add(new Commodity("洛川红富士苹果冰糖心10斤箱装", "SXLC001A", "11A", 44.80f, 3601, "红富士.jpg"));
        list.add(new Commodity("智利车厘子2斤大樱桃整箱顺丰包邮", "SHPD0A2B", "11G", 59.80f, 5420, "车厘子.jpg"));
        list.add(new Commodity("波士顿龙虾特大鲜活1斤", "LNDL0A3A", "13B", 149.00f, 2800, "龙虾.jpg"));
        model.addAttribute("commoditys", list);
        return "bootstrap";
    }
}
