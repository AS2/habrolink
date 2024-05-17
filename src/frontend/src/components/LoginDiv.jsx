import { useCallback } from "react";
import { useNavigate } from "react-router-dom";
import styles from "./LoginDiv.module.css";
import Form from 'react-bootstrap/Form';

const LoginDiv = () => {
  const navigate = useNavigate();

  const onButtonStyle1Click = useCallback(() => {
    const requestData = {
      email: state.makeGaussianBlur,
      password: state.gaussianBlurCount,
    };

    fetch('localhost:8000/user/signin', {
      method: 'POST',
      body: "username=aabb@x.com&password=aabb",
      headers: {
        'Content-type': 'application/x-www-form-urlencoded',
      },
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        // Handle data
      })
      .catch((err) => {
        console.log(err.message);
      });

    navigate("/user-profile");
  }, [navigate]);

  const onText1Click = useCallback(() => {
    navigate("/signup");
  }, [navigate]);

  return (
    <div className={styles.loginDiv}>
      <b className={styles.b}>Войти в систему</b>
      <Form>
        <Form.Group className="mb-3" controlId="exampleForm.ControlInput1">
          <Form.Control type="email" placeholder="name@example.com" id="emailInput" />
          <Form.Control type="password" placeholder="Password" id="pwInput" />
          <Form.Control type="submit" onClick={onButtonStyle1Click} />
        </Form.Group>
      </Form>
      <div className={styles.div1}>
        <i className={styles.b}>Нет записи?</i>
        <div className={styles.div2} onClick={onText1Click}>
          <span className={styles.span}>Создайте</span>
          <span> её.</span>
        </div>
      </div>
    </div>
  );
};

export default LoginDiv;
