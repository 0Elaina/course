package com.demo.entity;

import jakarta.validation.constraints.DecimalMin;
import jakarta.validation.constraints.Digits;
import jakarta.validation.constraints.Max;
import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Pattern;
import jakarta.validation.constraints.Positive;
import jakarta.validation.constraints.Size;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class ValidCommodity {

    @NotNull(message = "必须输入商品号")
    @Positive(message = "必须为正值")
    private Integer pid;        // 商品号

    @NotBlank(message = "必须输入名称")
    private String pname;       // 商品名称

    @Pattern(regexp = "^[0-9]{2}[A-Za-z]$", message = "分类编码不合法")
    private String tcode;       // 商品分类

    @NotNull(message = "必须输入价格")
    @DecimalMin(value = "0.01", message = "价格必须大于0")
    @Digits(integer = 5, fraction = 2, message = "精度不合要求")
    private Float pprice;       // 商品价格

    @NotNull(message = "必须输入库存")
    @Min(value = 0, message = "库存不能为负")
    @Max(value = 100000, message = "库存超范围")
    private Integer stocks;     // 库存量

    @Size(max = 25, message = "内容过于冗长")
    private String textadv;     // 推广文字
}
