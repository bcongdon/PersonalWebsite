import fitbit, json, os

loc = os.path.join(os.getcwd(), 'app','fitbit','user_settings.txt')
tokenfile = loc

class StepGetter:
    client = None
    token = ""

    def __init__(self):
        z = fitbit.Fitbit();

        # Try to read existing token pair
        try:
            self.token = json.load(open(tokenfile))
        except IOError:
            # If not generate a new file
            # Get the authorization URL for user to complete in browser.
            auth_url = z.GetAuthorizationUri()
            print "Please visit the link below and approve the app:\n %s" % auth_url
            # Set the access code that is part of the arguments of the callback URL FitBit redirects to.
            access_code = raw_input("Please enter code (from the URL you were redirected to): ")
            # Use the temporary access code to obtain a more permanent pair of tokens
            token = z.GetAccessToken(access_code)
            # Save the token to a file
            json.dump(token, open(tokenfile,'w'))

            response = z.ApiCall(token, '/1/user/-/profile.json')
            self.token = response['token']
            json.dump(self.token, open(tokenfile,'w'))
        self.client = z

    def get_steps_since(self, date):
        steps = self.client.ApiCall(self.token, '/1/user/-/activities/steps/date/' + str(date) + '/today.json')
        total = 0
        for day in steps['activities-steps']:
            total += int(day['value'])
        return total