const formTypeHeader = 'application/x-www-form-urlencoded';
const csrfToken = document.querySelector('meta[name="csrf-token"]').content;


export const sendXMLHttpRequest = (method, url = window.location.href, data, contentTypeHeader = formTypeHeader) => {
    const promise = new Promise((resolve, reject) => {
        const xhr = new XMLHttpRequest();
        xhr.open(method, url);

        xhr.responseType = 'json';

        if (data) {
            xhr.setRequestHeader('Content-Type', contentTypeHeader);
        }

        xhr.setRequestHeader('X-CSRFToken', csrfToken);
        xhr.onload = () => {
            if (xhr.status >= 400) {
                reject(xhr.response);
            } else {
                resolve(xhr.response);
            }
        }

        xhr.onerror = () => {
            reject("Something went wrong: either you have no network connection or the server is offline.");
        }

        xhr.send(data);
    });
    return promise;
}