import { useCallback } from "react";
import LoginDiv from "../components/LoginDiv";
import { useNavigate } from "react-router-dom";
import styles from "./SignIn.module.css";

const SignIn = () => {
  const navigate = useNavigate();

  const onTextClick = useCallback(() => {
    navigate("/");
  }, [navigate]);

  return (
    <div className={styles.signin}>
      <LoginDiv />
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
    </div>
  );
};

export default SignIn;
