package com.nep.category.service.impl;

import java.util.List;

import org.springframework.stereotype.Service;

import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.nep.category.entity.Category;
import com.nep.category.mapper.CategoryMapper;
import com.nep.category.service.CategoryService;

import lombok.RequiredArgsConstructor;

@Service
@RequiredArgsConstructor
public class CategoryServiceImpl implements CategoryService {
    private final CategoryMapper categoryMapper;

    /**
     * 获取所有分类，按排序顺序和ID升序排序
     * @return 所有分类列表
     */
    @Override
    public List<Category> getAllCategories() {
        List<Category> categories = categoryMapper.selectList(new LambdaQueryWrapper<Category>()
                .orderByAsc(Category::getId));
        return categories;
    }
}
