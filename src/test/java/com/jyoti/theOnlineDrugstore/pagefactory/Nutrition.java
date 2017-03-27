package com.jyoti.theOnlineDrugstore.pagefactory;


import java.util.ArrayList;
import java.util.List;

import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class Nutrition {

	@FindBy(xpath=".//*[@id='PrimaryMenu']/ul/li[4]/a")
	private WebElement nutriSelect;
	
	@FindBy(xpath=".//*[@id='PrimaryMenu']/ul/li[4]/ul/li[3]/a")
	private WebElement vita;
	
	@FindBy(xpath=".//*[contains(text(),'Add To Cart')]")
	private List<WebElement> addToCart;
	
	@FindBy(xpath=".//*[@id='LayoutColumn1']/div[2]/form/ul/li")
	private List<WebElement> quickView;
	
	//exploring one product entirely
	@FindBy(xpath=".//*[@id='frmCompare']/ul/li[2]")
	private List<WebElement> welleseCalcium;
	
	public List<WebElement> welleseCalcium(){
		return welleseCalcium;
	}
	
	
	
	public WebElement nutriSelect(){
		
		return nutriSelect;
	}
	public WebElement vita(){
		return vita;
	}
	public List<WebElement> addToCart(){
		
		return new ArrayList<>(addToCart);
	}
	
   public List<WebElement> quickView(){
		
		return new ArrayList<>(quickView);
	}
}
