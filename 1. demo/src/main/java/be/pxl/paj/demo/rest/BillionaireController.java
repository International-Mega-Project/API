package be.pxl.paj.demo.rest;


import be.pxl.paj.demo.api.BillionaireDTO;
import be.pxl.paj.demo.api.BillionaireResource;
import be.pxl.paj.demo.service.BillionaireService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("billionaires")
public class BillionaireController {

    @Autowired
    private BillionaireService billionaireService;

    @GetMapping
    public List<BillionaireDTO> findAllBillionaires() {
        return billionaireService.findAllBillionaires();
    }

    @PostMapping
    public void createBillionaire(@RequestBody BillionaireResource billionaireResource){
        billionaireService.saveBillionair(billionaireResource);
    }

}
