package monster.update.pageFactory;

import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class Login_monster {

	@FindBy(xpath=".//*[@id='jobuser_wrap']/div[1]/div/div[1]/a[1]")
	private WebElement signIn;
	public WebElement signIn(){
		return signIn;
	}
	@FindBy(xpath=".//*[@id='username_login']")
	private WebElement userName;
	public WebElement userName(){
		return userName;
	}
	@FindBy(xpath=".//*[*[@class='form-group']]/div[4]")
	private WebElement password;
	public WebElement password(){
		return password;
	}
	@FindBy(xpath=".//*[@id='button']")
	private WebElement submit;
	public WebElement submit(){
		return submit;
	}
}
