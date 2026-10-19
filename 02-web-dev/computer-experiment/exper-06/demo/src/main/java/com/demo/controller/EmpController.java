package com.demo.controller;

import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.demo.api.ApiResponse;
import com.demo.dto.PageEmp;
import com.demo.dto.PageResult;
import com.demo.entity.Emp;
import com.demo.service.EmpService;

import lombok.RequiredArgsConstructor;

@RestController
@RequestMapping("/emps")
@RequiredArgsConstructor
public class EmpController {
    private final EmpService empService;

    @GetMapping
    public ApiResponse<PageResult<Emp>> page(
            PageEmp pageEmp) {
        return ApiResponse.success(
                empService.list(pageEmp));
    }

    @PostMapping
    public ApiResponse<Void> save(@RequestBody Emp emp) {
        empService.save(emp);
        return ApiResponse.success();
    }

    @PutMapping
    public ApiResponse<Void> update(@RequestBody Emp emp) {
        empService.update(emp);
        return ApiResponse.success();
    }

    @DeleteMapping
    public ApiResponse<Void> delete(@RequestParam Integer id) {
        empService.deleteById(id);
        return ApiResponse.success();
    }
}
