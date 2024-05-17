import { useCallback } from "react";
import { useNavigate } from "react-router-dom";
import LoginDiv from "../components/LoginDiv";
import styles from "./SignIn.module.css";

const SignIn = () => {
  const navigate = useNavigate();

  const onTextClick = useCallback(() => {
    navigate("/");
  }, [navigate]);

  return (
    <div className={styles.signin}>
      <div className={styles.header}>
        <b className={styles.b} onClick={onTextClick}>
          <span>{`{`}</span>
          <span className={styles.span}>Хабро:</span>
          <span>{`Линкер}`}</span>
        </b>
        <img
          className={styles.interfaceEssentialmagnifier}
          alt=""
          src="/interface-essentialmagnifier.svg"
        />
      </div>
      <LoginDiv />
    </div>
  );
};

export default SignIn;
