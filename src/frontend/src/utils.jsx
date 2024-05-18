import {BACKEND_LINK} from "./config";

export function HasToken()
{
    let token = localStorage.getItem('token')
    if (token == null)
        return false
    else
        return true
}

export function RemoveToken()
{
    localStorage.removeItem('token')
}

export async function SendToBackend(type, api, data)
{
    const requestOptions = {
        method: type,
        headers: {
            "accept": "application/json",
            "Content-Type": "application/json" },
        body: JSON.stringify(data)
    };

    const answer_text = await fetch(BACKEND_LINK + api, requestOptions);
    if (answer_text.status !== 200)
        return null
    const answer_json = await answer_text.json()
    return answer_json
}

export async function AuthenticateOnBack(username, password)
{
    const params = new URLSearchParams({
        grant_type:"",
        username: username,
        password: password,
        scope:"",
        client_id:"",
        client_secret:""
    });

    const requestOptions = {
        method: "POST",
        headers: {
            "accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded" },
        body: params.toString()
    };

    let result = {
        success : true,
        json : {},
        error : ""
    }

    const answer_text = await fetch(BACKEND_LINK + "/user/signin", requestOptions);
    if (answer_text.status !== 200) {
        result.success = false;
        result.error = answer_text.body.toString()
    }
    else {
        const answer_json = await answer_text.json()
        localStorage.setItem("token", answer_json["access_token"])
        result.json = answer_json
    }

    return result
}

export async function SendToBackendAuthorized(type, api, data)
{
    const requestOptions = {
        method: type,
        headers: {
            "accept": "application/json",
            "Content-Type": "application/json",
            "Authorization" : "Bearer " + localStorage.getItem('token')
        },
        body: JSON.stringify(data)
    };

    const answer_test = await fetch(BACKEND_LINK + api, requestOptions);
    if (answer_test.status !== 200)
        return null
    const answer_json = await answer_test.json()
    return answer_json
}