import requests
import constants
import course_class

def parse_to_html(html_file):
    '''Parse courses from Albert into data.html file.'''
    
    # Constants needed for the request
    url = "https://m.albert.nyu.edu/app/catalog/getClassSearch"
    payload='CSRFToken=0cacdd6a262ee0c2540ca0f1d44089d2&acad_group=UH&catalog_nbr=&class_nbr=&keyword=&nyu_location=&subject=&term=1224'
    headers = {
      'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
      'Accept': '*/*',
      'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
      'X-Requested-With': 'XMLHttpRequest',
      'sec-ch-ua-mobile': '?0',
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
      'sec-ch-ua-platform': '"macOS"',
      'Cookie': 'ADRUM=s=1636870439764&r=https%3A%2F%2Fbrightspace.nyu.edu%2Fd2l%2Flms%2Fdropbox%2Fuser%2Ffolder_user_view_feedback.d2l%3F150855492; BIGipServer~SNS-LOW~prod-sis-pool=rd3133o00000000000000000000ffff0a2f060co8066; ExpirePage=https://sis.portal.nyu.edu/psp/ihprod/; HPTabName=IS_SSS_TAB; HPTabNameRemote=; LastActiveTab=IS_SSS_TAB; PHPSESSID=3mstcj041d770t3aof5f447t52; PS_DEVICEFEATURES=width:1440 height:900 pixelratio:2 touch:0 geolocation:1 websockets:1 webworkers:1 datepicker:1 dtpicker:1 timepicker:1 dnd:1 sessionstorage:1 localstorage:1 history:1 canvas:1 svg:1 postmessage:1 hc:0 maf:0; PS_LASTSITE=https://sis.portal.nyu.edu/psp/ihprod/; PS_LOGINLIST=https://sis.nyu.edu/csprod https://sis.portal.nyu.edu/ihprod; PS_TOKEN=pQAAAAQDAgEBAAAAvAIAAAAAAAAsAAAABABTaGRyAk4Abwg4AC4AMQAwABTTIyhuXc421buKdmehGQ5pbbYAJmUAAAAFAFNkYXRhWXicJYpLDkBAEAXLEEs3IWNGfJYW2Mkk7MUJLFzP4TyjX6q6k34XkKUmSbQfQ5zi5KbGM9Aq+cTKQhHYmNk5CIw0DotTrRS/vezkSli5jvf37ZVO8AKCVAt8; PS_TOKENEXPIRE=14_Nov_2021_0:18_GMT; PS_TokenSite=https://sis.portal.nyu.edu/psp/ihprod/?pco01lw-1556s-8051-PORTAL-PSJSESSIONID; SignOnDefault=; __utma=57748789.1922840866.1628059481.1634405387.1635238799.10; __utmz=57748789.1634405387.9.9.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); _drip_client_6158192=vid%253D54db9895aa194ce784fc3ae4202d043c%2526pageViews%253D1%2526sessionPageCount%253D1%2526lastVisitedAt%253D392646895%2526weeklySessionCount%253D1%2526lastSessionAt%253D392646895; _fbp=fb.1.1628059634773.4892; _ga=GA1.2.1922840866.1628059481; _gid=GA1.2.1265445606.1636786654; _scid=71aa006a-23f4-42ea-890c-89907fa69fd4; _sctr=1|1635192000000; fpestid=S50C2-epUV24gCdlSadqrCOEpyczyqXcq5JUStKCxPPUNkP-2_ps6xbyuKkOfVNY6mLbdw; https%3a%2f%2fsis.portal.nyu.edu%2fpsp%2fihprod%2femployee%2fempl%2frefresh=list:%20%3Ftab%3Dremoteunifieddashboard%7C%3Frp%3Dremoteunifieddashboard%7C%7C%7C; lcsrftoken=hopTsZFqR3gKZ7dDdRhSzNX1Le2ImkVuOMdo+arSF7I=; nmstat=791ca8c8-78ab-1aed-df5c-5280f1b7d038; nyuad=eyJpdiI6InAwd0NwRlY2YjA3T01VYlN6VXRnN1E9PSIsInZhbHVlIjoiM1JHeWRxaEVjTW5XYW1jXC9BV2lQcUVGWHZhXC9DS2lIdHhSbnlnM1VwWnhPUjVsYzdXQVBmWUtLaTNoc1U0UTdhTFVEMittN3NnUGo5cHJHbzdBQW1tdz09IiwibWFjIjoiZWZmMDM4MzQ3MDZiZTQ1NGM2NjBkODZjNzBkYTNjZTQ1MTRkNTgwMTA4MDE1ZWI5YTdlN2YwYzJiODNjN2ZjMyJ9; pco01lw-1537s-8051-PORTAL-PSJSESSIONID=yAEdyHAO9VuqIwlgf9jAK87lXuRmxvEH!1483518525; pco01lw-1556s-8051-PORTAL-PSJSESSIONID=SM0dyGzyrYMhlq0-Q5RcjnLWMnP27kDu!-665168926; ps_theme=node:EMPL portal:EMPLOYEE theme_id:NYU_THEME accessibility:N formfactor:3 piamode:2; psback=%22%22url%22%3A%22https%3A%2F%2Fsis.portal.nyu.edu%2Fpsp%2Fihprod%2FEMPLOYEE%2FEMPL%2Fh%2F%3Ftab%3DIS_SSS_TAB%22%20%22label%22%3A%22LabelNotFound%22%20%22origin%22%3A%22PIA%22%20%22layout%22%3A%220%22%20%22refurl%22%3A%22https%3A%2F%2Fsis.portal.nyu.edu%2Fpsp%2Fihprod%2FEMPLOYEE%2FEMPL%2Fh%2F%3Ftab%3DIS_SSS_TAB%22%22; BIGipServer~SNS-LOW~prod-m-albert-pool=rd3133o00000000000000000000ffff0a2f060eo80; BIGipServer~SNS-LOW~prod-sis-portal-pool=rd3133o00000000000000000000ffff0a2f0614o8666; CSRFCookie=0cacdd6a262ee0c2540ca0f1d44089d2; _ga=GA1.4.1922840866.1628059481; _gid=GA1.4.1265445606.1636786654; highpoint_cs=rb7j695s1t5irkrqec3etmn3t2'
    }

    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        
        # saving into data.html file
        html_file = open(html_file, 'w')
        html_file.write(response.text)
        html_file.close()
        
        # saving the latest version into the backup file
        backup_file = open(constants.BACKUP_HTML ,'w')
        backup_file.write(response.text)
        backup_file.close()

    except requests.exceptions.RequestException as e: # Error of not being able to parse data
        print('Error')

        # copying contents from backup file into the data.html file
        with open(constants.BACKUP_HTML,'r') as firstfile, open(html_file, 'w') as secondfile:
            for line in firstfile:
                secondfile.write(line) 

if __name__ == '__main__':
    parse_to_html(constants.COURSES_HTML)