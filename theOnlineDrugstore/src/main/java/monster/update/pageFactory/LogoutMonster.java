package monster.update.pageFactory;

import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class LogoutMonster {

	@FindBy(xpath=".//*[@id='mnuser_nav']/li[6]/a/img")
	private WebElement logoutImg;
	public WebElement logoutImg(){
		return logoutImg;
	}
	@FindBy(xpath=".//*[@id='mnuser_nav']/li[6]/ul/li[4]/a[3]")
	private WebElement logout;
	public WebElement logout(){
		return logout;
	}
}
