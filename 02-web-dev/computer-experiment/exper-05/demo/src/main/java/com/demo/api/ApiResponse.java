package com.demo.api;

import lombok.AllArgsConstructor;
import lombok.Data;

@Data
@AllArgsConstructor
public class ApiResponse<T> {
    private T data;
    private String code;
    private String message;

    public static <T> ApiResponse<T> success(T data) {
        return new ApiResponse<T>(
                data, "200", "success");
    }

    public static ApiResponse<Void> error(String code) {
        return new ApiResponse<Void>(null, code, "error");
    }
}
