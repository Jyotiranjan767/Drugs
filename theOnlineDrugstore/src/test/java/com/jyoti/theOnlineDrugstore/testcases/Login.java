package com.jyoti.theOnlineDrugstore.testcases;

import org.testng.annotations.Test;

import com.jyoti.theOnlineDrugstore.BusinessClass.BusinessComponents;
import com.jyoti.theOnlineDrugstore.ExcelLib.Driver;

public class Login {

	BusinessComponents bc=new BusinessComponents();
	@Test(priority=1)
	public void login() throws InterruptedException{
		
		Driver.driver.get("http://theonlinedrugstore.com");
		bc.logBusi();
		//Driver.driver.close();
		bc.addToCart();
	}
	@Test(priority=21)
	public void nutriBags(){
		bc.nutriBags();
	}
	@Test(priority=342)
	public void addToCart(){
		bc.addToCart();
	}
}
