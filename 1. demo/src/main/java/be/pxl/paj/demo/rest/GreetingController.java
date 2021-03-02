package be.pxl.paj.demo.rest;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class GreetingController {
    @GetMapping("hello")
    public String doGreeting() {
        return "hello!";
    }
}
