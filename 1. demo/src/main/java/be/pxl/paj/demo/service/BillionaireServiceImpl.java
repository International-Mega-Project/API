package be.pxl.paj.demo.service;

import be.pxl.paj.demo.api.BillionaireDTO;
import be.pxl.paj.demo.api.BillionaireResource;
import be.pxl.paj.demo.domain.Billionaire;
import be.pxl.paj.demo.repository.BillionairRepository;
import jdk.dynalink.linker.LinkerServices;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

@Service
public class BillionaireServiceImpl implements BillionaireService{

    @Autowired
    private BillionairRepository billionairRepository;


    public void saveBillionair(BillionaireResource billionaireResource) {
        Billionaire newBillionare = new Billionaire();
        newBillionare.setName(BillionaireResource.getName());
        newBillionare.setFirstName(BillionaireResource.getFirstName());
        newBillionare.setCountry(BillionaireResource.getCountry());
        billionairRepository.save(newBillionare);
    }

    public List<BillionaireDTO> findAllBillionaires() {
        return billionairRepository.findAll().stream().map(BillionaireDTO::new).collect(Collectors.toList());
    }
}
