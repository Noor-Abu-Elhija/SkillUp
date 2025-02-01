import asyncio
from playwright.async_api import async_playwright
import json
import pandas as pd

async def scrape_glassdoor():
    job_data = []
    urls = ["https://www.glassdoor.co.in/Job/us-usa-jobs-SRCH_IL.0,2_IN1_KO3,6.htm",
            "https://www.glassdoor.com/Job/united-states-united-states-jobs-SRCH_IL.0,13_IN1_KO14,27.htm",
            "https://www.glassdoor.com/Job/united-states-america-jobs-SRCH_IL.0,13_IN1_KO14,21.htm",
            "https://www.glassdoor.com/Job/united-states-usa-jobs-SRCH_IL.0,13_IN1_KO14,17.htm",
            "https://www.glassdoor.com/Job/united-states-jobs-in-usa-jobs-SRCH_IL.0,13_IN1_KO14,25.htm",
            "https://www.glassdoor.com/Job/united-states-job-in-united-states-jobs-SRCH_IL.0,13_IN1_KO14,34.htm",
            "https://www.glassdoor.com/Job/united-states-remote-jobs-SRCH_IL.0,13_IN1_KO14,20.htm",
            "https://www.glassdoor.com/Job/united-states-senior-roles-jobs-SRCH_IL.0,13_IN1_KO14,26.htm",
            "https://www.glassdoor.com/Job/united-states--fresh-graduates-jobs-SRCH_IL.0,13_IN1_KO14,30.htm",
            "https://www.glassdoor.com/Job/united-states-work-from-anywhere-jobs-jobs-SRCH_IL.0,13_IN1_KO14,37.htm",
            "https://www.glassdoor.com/Job/united-states-hybrid-jobs-usa-jobs-SRCH_IL.0,13_IN1_KO14,29.htm",
            "https://www.glassdoor.com/Job/jobs.htm?sc.occupationParam=USA-Based+Jobs+Open+to+emote&sc.locationSeoString=United+States&locId=1&locT=N",
            "https://www.glassdoor.com/Job/united-states-jobs-hiring-in-usa-jobs-SRCH_IL.0,13_IN1_KO14,32.htm"
            "https://www.glassdoor.com/Job/jobs.htm?sc.occupationParam=On-Site+Jobs+in+USA&sc.locationSeoString=United+States&locId=1&locT=N"
            "https://www.glassdoor.com/Job/united-states-specialist-roles-jobs-jobs-SRCH_IL.0,13_IN1_KO14,35.htm",
            "https://www.glassdoor.com/Job/united-states-no-location-restriction-jobs-usa-jobs-SRCH_IL.0,13_IN1_KO14,46.htm",
            "https://www.glassdoor.com/Job/united-states-work-from-home-opportunities-usa-jobs-SRCH_IL.0,13_IN1_KO14,46.htm",
            "https://www.glassdoor.com/Job/united-states--jobs-available-in-usa-jobs-SRCH_IL.0,13_IN1_KO14,36.htm",
           ]
    for url in  urls:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)
            page = await browser.new_page()


            await page.goto(url)
            print(f"Accessing: {url}")


            first_click = True
            while True:
                try:
                    print("Looking for 'Show More Jobs' button...")


                    show_more_button = await page.query_selector(
                        "#left-column > div.JobsList_wrapper__EyUF6 > div > div"
                    )
                    if show_more_button:
                        print("Clicking 'Show More Jobs' button...")
                        await show_more_button.click()
                        await asyncio.sleep(3)


                        if first_click:
                            first_click = False
                            while True:
                                print("Checking for popup...")
                                popup_close_button = await page.query_selector(
                                    "body > div.ModalContainer > div.Modal > div.ContentAndBottomSection > div.ContentSection > div > div.closeButtonWrapper > button"
                                )
                                if popup_close_button:
                                    print("Closing popup...")
                                    await popup_close_button.click()
                                    await asyncio.sleep(2)

                                else:
                                    print("Popup not found.")
                                    break
                    else:
                        print("No more 'Show More Jobs' button. All jobs loaded.")
                        break
                except Exception as e:
                    print(f"Error clicking 'Show More Jobs': {e}")
                    break


            print("Scraping all jobs...")
            await page.wait_for_selector("#left-column > div.JobsList_wrapper__EyUF6 > ul")
            job_list_container = await page.query_selector("#left-column > div.JobsList_wrapper__EyUF6 > ul")

            if not job_list_container:
                print("Job list container not found. Exiting.")
                return []


            job_cards = await job_list_container.query_selector_all('li.JobsList_jobListItem__wjTHv')
            print(f"Found {len(job_cards)} jobs on the page.")



            for index, job_card in enumerate(job_cards):
                try:
                    print(f"Scraping job {index + 1}/{len(job_cards)}...")


                    await job_card.scroll_into_view_if_needed()


                    title_element = await job_card.query_selector("a")
                    title = await title_element.inner_text() if title_element else "N/A"


                    await job_card.click()
                    await asyncio.sleep(2)

                    # Extract the job location
                    location_element = await page.query_selector(
                        "#app-navigation > div.PageContainer_pageContainer__CVcfg.Page_fullHeight__QlatA > div.TwoColumnLayout_container___jk7P.TwoColumnLayout_serp__pCNV6 > div.TwoColumnLayout_columnRight__GRvqO > div > div.JobDetails_jobDetailsContainer__y9P3L > header > div.JobDetails_jobDetailsHeader__Hd9M3 > div.JobDetails_location__mSg5h"
                    )
                    location = await location_element.inner_text() if location_element else "N/A"


                    try:
                        show_more_button = await page.query_selector(
                            "#app-navigation > div.PageContainer_pageContainer__CVcfg.Page_fullHeight__QlatA > div.TwoColumnLayout_container___jk7P.TwoColumnLayout_serp__pCNV6 > div.TwoColumnLayout_columnRight__GRvqO > div > div.JobDetails_jobDetailsContainer__y9P3L > section > div.JobDetails_jobDescriptionWrapper___tqxc.JobDetails_jobDetailsSectionContainer__o_x6Z > div.JobDetails_showMoreWrapper__ja2_y > button"
                        )
                        if show_more_button:
                            print(f"Clicking 'Show More' for job {index + 1}")
                            await show_more_button.click()
                            await asyncio.sleep(1)
                    except Exception as e:
                        print(f"No 'Show More' button for job {index + 1}. Proceeding.")


                    description_element = await page.query_selector(
                        "#app-navigation > div.PageContainer_pageContainer__CVcfg.Page_fullHeight__QlatA > div.TwoColumnLayout_container___jk7P.TwoColumnLayout_serp__pCNV6 > div.TwoColumnLayout_columnRight__GRvqO > div > div.JobDetails_jobDetailsContainer__y9P3L > section > div.JobDetails_jobDescriptionWrapper___tqxc.JobDetails_jobDetailsSectionContainer__o_x6Z > div.JobDetails_jobDescription__uW_fK.JobDetails_showHidden__C_FOA"
                    )
                    description = await description_element.inner_text() if description_element else "N/A"


                    job_data.append({
                        "Job Title": title.strip(),
                        "Location": location.strip(),
                        "Description": description.strip()
                    })
                    print(f"Scraped: {title.strip()} | {location.strip()}")

                except Exception as e:
                    print(f"Error scraping job {index + 1}: {e}")
                    continue

            await browser.close()
    return job_data



async def main():
        job_data = await scrape_glassdoor()


        df = pd.DataFrame(job_data)


        df.to_parquet("glassdoor_jobs.parquet", index=False, engine="pyarrow")
        print("Job data saved to glassdoor_jobs.json!")



if __name__ == "__main__":
        asyncio.run(main())