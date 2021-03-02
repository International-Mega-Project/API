package be.pxl.paj.demo.api;

import be.pxl.paj.demo.domain.Billionaire;

public class BillionaireDTO {
	private Long id;
	private String firstName;
	private String name;
	private String country;

	public BillionaireDTO(Billionaire billionaire) {
		this.id = billionaire.getId();
		this.firstName = billionaire.getFirstName();
		this.name = billionaire.getName();
		this.country = billionaire.getCountry();
	}

	public Long getId() {
		return id;
	}

	public void setId(Long id) {
		this.id = id;
	}

	public String getFirstName() {
		return firstName;
	}

	public void setFirstName(String firstName) {
		this.firstName = firstName;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getCountry() {
		return country;
	}

	public void setCountry(String country) {
		this.country = country;
	}
}
