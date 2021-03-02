package be.pxl.paj.demo.repository;

import be.pxl.paj.demo.domain.Billionaire;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface BillionairRepository extends JpaRepository<Billionaire, Long> {

}
