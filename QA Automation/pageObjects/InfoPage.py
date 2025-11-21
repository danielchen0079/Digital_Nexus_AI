from playwright.sync_api import Page

class InfoPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.real_name_input = page.locator("#profile_truename")
        self.sex_male = page.locator("#profile_gender_0")
        self.sex_female = page.locator("#profile_gender_1")
        self.id_number_input = page.locator("#profile_idcard")
        self.phone_input = page.locator("#profile_mobile")
        self.company_input = page.locator("#profile_company")
        self.job_input = page.locator("#profile_job")
        self.title_input = page.locator("#profile_title")
        self.signature_input = page.locator("#profile_signature")
        self.self_intro_frame = page.frame_locator("iframe.cke_wysiwyg_frame.cke_reset")
        self.self_intro_input = self.self_intro_frame.locator(
            "body.cke_editable.cke_editable_themed.cke_contents_ltr"
        )
        self.site_input = page.locator("#profile_site")
        self.weibo_input = page.locator("#weibo")
        self.wechat_input = page.locator("#profile_weixin")
        self.qq_input = page.locator("#profile_qq")
        self.submit_button = page.locator("#profile-save-btn")

    def fill_info(
        self,
        real_name: str,
        sex: str,
        id_num: str,
        phone: str,
        company: str,
        job: str,
        title: str,
        signature: str,
        intro: str,
        site: str,
        weibo: str,
        wechat: str,
        qq: str,
    ) -> None:
        self.real_name_input.fill(real_name)
        if sex.lower() == "male":
            self.sex_male.check()
        else:
            self.sex_female.check()
        self.id_number_input.fill(id_num)
        self.phone_input.fill(phone)
        self.company_input.fill(company)
        self.job_input.fill(job)
        self.title_input.fill(title)
        self.signature_input.fill(signature)
        self.self_intro_input.fill(intro)
        self.site_input.fill(site)
        self.weibo_input.fill(weibo)
        self.wechat_input.fill(wechat)
        self.qq_input.fill(qq)
        self.submit_button.click()
