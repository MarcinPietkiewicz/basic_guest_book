function validateComment() {

    let name = document.getElementById('name').value;
    let comment = document.getElementById('comment').value;
    let email = document.getElementById('email').value;
    console.log(name);
    console.log(comment);
    console.log(email);
    console.log('sprawdzam poprawność...')

    if (name.length < 3) {
        console.log("imię powinno mieć więcej niż 3 znaki!");
        return false;
    }
    if (comment.length <= 10) {
        console.log('Komentarz ma mieć więcej niż 10 znaków!')
        return false;
    }
    if (!/^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/i.test(email)) {
        console.log('Format emaila nieprawidłowy!')
        return false;
    }
//    else if (\b(?:(?:https?|ftp|file):\/\/|www\.|ftp\.)(?:\([-A-Z0-9+&@#/%=~_|$?!:,.]*\)|[-A-Z0-9+&@#/%=~_|$?!:,.])*?:\([-A-Z0-9+&@#/%=~_|$?!:,.]*\)|[A-Z0-9+&@#/%=~_|$].test(comment)) {
//        console.log('Komentarz zawiera linki lub emaile!')
//        return false;
//    }
    regex = /[<>!@#$%^&*(),.?":{}|<>]/
    if (regex.test(comment)) {
        console.log('Komentarz zawiera niedozwolone znaki HTML!')
        return false;
    }
    if (comment.length > 100) {
        console.log('Komentarz ma więcej niż 100 znaków. Spróbuj skrócić komentarz')
        return false;
    }
    return true;
}

