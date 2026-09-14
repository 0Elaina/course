package com.nep.common.exception;

import org.springframework.http.ResponseEntity;
import org.springframework.validation.FieldError;
import org.springframework.http.converter.HttpMessageNotReadableException;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.RestControllerAdvice;

import com.nep.common.ApiCode;
import com.nep.common.Result;

import lombok.extern.slf4j.Slf4j;

@Slf4j
@RestControllerAdvice
public class GlobalExceptionHandler {

    /**
     * 处理业务异常
     * 
     * @param e 业务异常
     * @return 异常结果
     */
    @ExceptionHandler(BusinessException.class)
    public ResponseEntity<Result<Void>> handleBusinessException(BusinessException e) {
        ApiCode apiCode = e.getApiCode();
        return ResponseEntity.status(apiCode.getStatus())
                .body(Result.error(apiCode.getCode(), apiCode.getMessage()));
    }

    /**
     * 处理参数校验异常
     * 
     * @param e 参数校验异常
     * @return 异常结果
     */
    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<Result<Void>> handleValidationException(MethodArgumentNotValidException e) {
        String message = e.getBindingResult().getFieldErrors().stream()
                .map(FieldError::getDefaultMessage)
                .filter(value -> value != null & !value.isBlank())
                .findFirst()
                .orElse("参数校验失败");
        return ResponseEntity.badRequest()
                .body(Result.error(ApiCode.BAD_REQUEST.getCode(), message));
    }

    /**
     * 处理请求体格式错误异常
     * 
     * @param e 请求体格式错误异常
     * @return 异常结果
     */
    @ExceptionHandler(HttpMessageNotReadableException.class)
    public ResponseEntity<Result<Void>> handleUnReadableException(HttpMessageNotReadableException e) {
        return ResponseEntity.badRequest()
                .body(Result.error(ApiCode.BAD_REQUEST.getCode(), "请求体格式错误"));
    }

    /**
     * 处理服务器内部错误异常
     * 
     * @param e 服务器内部错误异常
     * @return 异常结果
     */
    @ExceptionHandler(Exception.class)
    public ResponseEntity<Result<Void>> handleException(Exception e) {
        log.error("服务器内部错误", e);
        ApiCode apiCode = ApiCode.INTERNAL_SERVER_ERROR;
        return ResponseEntity.status(apiCode.getStatus())
                .body(Result.error(apiCode.getCode(), apiCode.getMessage()));
    }
}
