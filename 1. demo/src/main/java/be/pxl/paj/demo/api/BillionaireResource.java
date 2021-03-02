package be.pxl.paj.demo.api;

public class BillionaireResource {
	private static String firstName;
	private static String name;
	private static String country;

	public static String getFirstName() {
		return firstName;
	}

	public void setFirstName(String firstName) {
		this.firstName = firstName;
	}

	public static String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public static String getCountry() {
		return country;
	}

	public void setCountry(String country) {
		this.country = country;
	}
}
