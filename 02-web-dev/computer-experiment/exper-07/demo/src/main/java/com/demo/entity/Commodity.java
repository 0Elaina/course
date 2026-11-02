package com.demo.entity;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class Commodity {
    private String pname;    // 商品名称
    private String scode;    // 商家编码
    private String tcode;    // 商品分类编码
    private Float pprice;    // 商品价格
    private Integer stocks;  // 商品库存
    private String image;    // 商品图片
}
