package com.demo.controller;

import com.demo.entity.Category;
import com.demo.entity.Commodity;
import com.demo.entity.Supplier;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Date;
import java.util.List;

@Controller
@RequestMapping("/th")
public class ViewController {

    // 1. 显示文本（th:text）
    @RequestMapping("/text")
    public String showText(Model model, @RequestParam(name = "sname", required = false) String sname) {
        model.addAttribute("name", sname);
        return "th/text";
    }

    // 2. 显示对象（th:object）
    @RequestMapping("/object")
    public String showObject(Model model, Supplier supplier) {
        // 如果没有传入参数，则赋予默认演示数据
        if (supplier.getSname() == null && supplier.getSweixin() == null) {
            supplier.setSname("陕西洛川苹果有限公司");
            supplier.setSweixin("8123456-aa.com");
        }
        model.addAttribute("sup", supplier);
        return "th/object";
    }

    // 3. 表单输入提交（th:field、th:name/th:value）
    @RequestMapping("/input")
    public String showInput(Model model, Supplier supplier) {
        supplier.setSname("陕西洛川苹果有限公司");
        supplier.setSweixin("8123456-aa.com");
        model.addAttribute("sup", supplier);
        return "th/input";
    }

    // 4. 超链接（th:href）
    @RequestMapping("/href")
    public String showHref() {
        return "th/href";
    }

    // 5. 条件判断（th:switch、th:if/th:unless）
    @RequestMapping("/switch")
    public String showSwitch(Model model, Category category) {
        model.addAttribute("cate", category);
        return "th/switch";
    }

    // 6. 字符串处理（+、|...|、#strings、==/!=、eq/ne/gt...）
    @RequestMapping("/strings")
    public String showStrings(Model model, Category category) {
        model.addAttribute("cate", category);
        return "th/strings";
    }

    // 7. 循环遍历（th:each）
    @RequestMapping("/each")
    public String showEach(Model model) {
        List<Commodity> list = new ArrayList<>();
        list.add(new Commodity("洛川红富士苹果冰糖心10斤箱装", "SXLC001A", "11A", 44.80f, 3601, "红富士.jpg"));
        list.add(new Commodity("智利车厘子2斤大樱桃整箱顺丰包邮", "SHPD0A2B", "11G", 59.80f, 5420, "车厘子.jpg"));
        list.add(new Commodity("波士顿龙虾特大鲜活1斤", "LNDL0A3A", "13B", 149.00f, 2800, "龙虾.jpg"));
        model.addAttribute("commoditys", list);
        return "th/each";
    }

    // 8. 公用对象（#dates、#numbers、#lists、#strings 等）
    @RequestMapping("/utility")
    public String testUtility(Model model) {
        model.addAttribute("currentDate", new Date());
        model.addAttribute("price", 1234567.89);
        model.addAttribute("rawString", "  Hello Thymeleaf Framework!  ");
        model.addAttribute("fruits", Arrays.asList("洛川苹果", "智利樱桃", "海南芒果", "波士顿龙虾"));
        model.addAttribute("isEnabled", true);
        return "th/utility";
    }
}
