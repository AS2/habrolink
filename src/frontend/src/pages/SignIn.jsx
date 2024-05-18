import {useCallback, useState} from "react";
import {useNavigate} from "react-router-dom";
import styles from "./SignIn.module.css";
import Header from "../components/Header";
import Form from "react-bootstrap/Form";
import {AuthenticateOnBack} from "../utils";

const SignIn = () => {
    const navigate = useNavigate();

    const [errorMsg, setErrorMsg] = useState("");

    const onTextClick = useCallback(() => {
        navigate("/");
    }, [navigate]);

    const onFormSubmit = useCallback(e => {
        e.preventDefault()
        const formData = new FormData(e.target),
            formDataObj = Object.fromEntries(formData.entries())

        async function Authenticate() {
            let response = await AuthenticateOnBack(formDataObj["email"], formDataObj["password"])
            if (response.success) {
                navigate("/");
            } else {
                setErrorMsg("Неверное имя пользователя или пароль")
            }
        }

        Authenticate()
    }, [navigate]);

    const onCreateNew = useCallback(() => {
        navigate("/");
    }, [navigate]);

    return (
        <div className={styles.signin}>
            <Header/>
            <div className={styles.loginDiv}>
                <b>Войти в систему</b>
                <Form onSubmit={onFormSubmit}>
                    <Form.Group className="mb-3">
                        <Form.Control type="email" placeholder="Email" name="email"/>
                        <Form.Control type="password" placeholder="Password" name="password"/>
                        <Form.Control type="submit"/>
                    </Form.Group>
                </Form>
                {errorMsg !== "" &&
                    <p className={styles.error}>
                        {errorMsg}
                    </p>}
                <div className={styles.createNewHint}>
                    <i>Нет записи?</i>
                    <div className={styles.createNewButton} onClick={onCreateNew}>
                        Создайте её.
                    </div>
                </div>
            </div>
        </div>
    );
};

export default SignIn;
