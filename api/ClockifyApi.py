import requests, json

CLOCKIFY_API_URL = "https://api.clockify.me/api/"

class ClockifyApi:
    """Wrapperobject for connecting to the clockify api."""

    def __init__(self, api_key, workspace_name):
        """ Constructor for the ClockifyApi.

        Takes a api_key := string, workspace_name := string.
        """
        self.api_key = api_key
        self.workspace_id = self.get_workspace_id(workspace_name)
        try:
            assert self.workspace_id != "No workspace found."
        except AssertionError as e:
            print(self.workspace_id[:-1] + " with name " + workspace_name +
                  " found")
            raise(e)


    def get_workspace_id(self, workspace_name):
        """Return string.

        Takes workspace_name := string. Gets the unique id string for
        the given workspace_name, associated to the given api_key.
        """
        header = {"content-type": "json", "X-Api-Key": self.api_key}
        data = requests.get(CLOCKIFY_API_URL + "/workspaces/",
                                    headers=header).json()
        for elem in data:
            try:
                if elem["name"] == workspace_name:
                    return elem["id"]

            except KeyError as e:
                raise(e)

        return "No workspace found."


if __name__ == "__main__":
    print("Hello World!")
