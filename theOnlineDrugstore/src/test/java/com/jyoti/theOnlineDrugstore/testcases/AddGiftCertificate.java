package com.jyoti.theOnlineDrugstore.testcases;

import org.testng.annotations.Test;

import com.jyoti.theOnlineDrugstore.BusinessClass.BusinessComponents;
import com.jyoti.theOnlineDrugstore.ExcelLib.Driver;

public class AddGiftCertificate {

	BusinessComponents bc=new BusinessComponents();
	@Test
	public void clickMainLink() throws InterruptedException{
		Driver.driver.get("http://theonlinedrugstore.com");
		bc.logBusi();
		bc.addGifts();
	}
}
