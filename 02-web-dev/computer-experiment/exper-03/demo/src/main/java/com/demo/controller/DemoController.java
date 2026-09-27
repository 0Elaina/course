package com.demo.controller;

import java.util.List;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.demo.entity.Book;

import io.swagger.v3.oas.annotations.Operation;

@RestController
public class DemoController {
    Book book1 = new Book("1", "1", 1L, 1);

    @Operation(summary = "根据图书 ID 查询图书详情")
    @GetMapping("/{bookId}")
    public String getByBookId(@PathVariable Long bookId) {
        return "bookId: " + bookId;
    }

    @Operation(summary = "按图书名关键词搜索图书")
    @GetMapping
    public String getByKeyword(
            @RequestParam String keyword,
            @RequestParam Integer pageNum) {
        return "OK" + keyword + pageNum;
    }

    @Operation(summary = "表单提交新增借阅详情")
    @PostMapping("/create")
    public Book createNewBook(Book book) {
        return new Book(book.getReaderName(), book.getPhone(), book.getBookId(), book.getDays());
    }

    @Operation(summary = "批量删除选中的借阅详情")
    @PostMapping("/deleteBatch")
    public String deleteBatch(@RequestParam List<Long> ids) {
        String result = "";
        for (Long id : ids) {
            result = result + id + " ";
        }
        return result;
    }

    @Operation(summary = "JSON新增图书信息")
    @PostMapping
    public String create(@RequestBody Book book) {
        return book.toString();
    }

}