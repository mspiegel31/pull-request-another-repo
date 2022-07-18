import gidgethub.httpx
import httpx

async with httpx.AsyncClient() as client:
    gh = gidgethub.httpx.GitHubAPI(client, requester, oauth_token=oauth_token)
    # Make your requests, e.g. ...
    data = await gh.getitem("/rate_limit")
