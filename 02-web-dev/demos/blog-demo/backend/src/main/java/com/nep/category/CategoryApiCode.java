package com.nep.category;

import org.springframework.http.HttpStatus;

import com.nep.common.ApiCode;

public final class CategoryApiCode {
    private CategoryApiCode() {
    }

    public static final ApiCode CATEGORY_NAME_DUPLICATE = new ApiCode(HttpStatus.CONFLICT, "CATEGORY_NAME_DUPLICATE",
            "分类名称已存在");
    

}
