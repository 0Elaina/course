package com.demo.entity;

public class Book {
    private String readerName;
    private String phone;
    private Long bookId;
    private Integer days;

    public Book(){

    }

    public Book(String readerName, String phone, Long bookId, Integer days) {
        this.readerName = readerName;
        this.phone = phone;
        this.bookId = bookId;
        this.days = days;
    }

    public void setReaderName(String readerName) {
        this.readerName = readerName;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }

    public void setBookId(Long bookId) {
        this.bookId = bookId;
    }

    public void setDays(Integer days) {
        this.days = days;
    }

    public String getReaderName() {
        return this.readerName;
    }

    public String getPhone() {
        return this.phone;
    }

    public Long getBookId() {
        return this.bookId;
    }

    public Integer getDays() {
        return this.days;
    }

    public String toString() {
        return "[Book]: {readerName: " + this.readerName + ", phone: " + this.phone
                + ", bookId: " + this.bookId + ", days: " + this.days;
    }
}
