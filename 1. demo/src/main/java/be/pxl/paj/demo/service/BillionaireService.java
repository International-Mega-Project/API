package be.pxl.paj.demo.service;

import be.pxl.paj.demo.api.BillionaireDTO;
import be.pxl.paj.demo.api.BillionaireResource;

import java.util.List;

public interface BillionaireService {
    void saveBillionair(BillionaireResource billionaireResource);
    List<BillionaireDTO> findAllBillionaires();

}
