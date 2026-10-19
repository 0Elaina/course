package com.demo.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.demo.api.ApiResponse;
import com.demo.entity.Dept;
import com.demo.service.DeptService;

import lombok.RequiredArgsConstructor;

@RestController
@RequestMapping("/dept")
@RequiredArgsConstructor
public class DeptController {
    private final DeptService deptService;

    @GetMapping("/{id}")
    public ApiResponse<Dept> getById(@PathVariable Integer id) {
        return ApiResponse.success(deptService.getById(id));
    }

    @PutMapping
    public ApiResponse<Void> update(@RequestBody Dept dept) {
        deptService.update(dept);
        return ApiResponse.success(null);
    }
}
