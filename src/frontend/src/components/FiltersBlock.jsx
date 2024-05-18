import { useCallback } from "react";
import StyleOutlineTypetextClea from "./StyleOutlineTypetextClea";
import styles from "./FiltersBlock.module.css";

import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';
import Row from 'react-bootstrap/Row';

const FiltersBlock = ({ onSubmitClick }) => {

  return (
    <div className={styles.filtersBlock}>

      <div className={styles.userPlatform}>
        <b className={styles.b}>Откуда пользователь?</b>
        <div className={styles.platformList}>
          <div class="form-check">
            <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault1" />
            <label class="form-check-label" for="flexRadioDefault1">С ХабраЛинкера</label>
          </div>
          <div class="form-check">
            <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault2" />
            <label class="form-check-label" for="flexRadioDefault2">С Хабра</label>
          </div>
          <div class="form-check">
            <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault3" />
            <label class="form-check-label" for="flexRadioDefault3">С любой платформы</label>
          </div>
        </div>
      </div>

      <b className={styles.b}>Рейтинг Хабра</b>
      <Form>
        <Form.Group as={Row} className="mb-3" controlId="minRating">
          <Form.Label column sm="2">
            Min:
          </Form.Label>
          <Col sm="10">
            <Form.Control type="number" defaultValue="0.0" />
          </Col>
        </Form.Group>

        <Form.Group as={Row} className="mb-3" controlId="maxRating">
          <Form.Label column sm="2">
            Max:
          </Form.Label>
          <Col sm="10">
            <Form.Control type="number" defaultValue="5.0" />
          </Col>
        </Form.Group>
      </Form>

      <b className={styles.b}>Карма Хабра</b>
      <Form>
        <Form.Group as={Row} className="mb-3" controlId="minCarma">
          <Form.Label column sm="2">
            Min:
          </Form.Label>
          <Col sm="10">
            <Form.Control type="number" defaultValue="0.0" />
          </Col>
        </Form.Group>

        <Form.Group as={Row} className="mb-3" controlId="maxCarma">
          <Form.Label column sm="2">
            Max:
          </Form.Label>
          <Col sm="10">
            <Form.Control type="number" defaultValue="300.0" />
          </Col>
        </Form.Group>
      </Form>
      <div className={styles.userPlatform}>
        <b className={styles.b}>Пол</b>
        <div class="form-check">
          <input class="form-check-input" type="radio" name="flexRadioDefault" id="sexRatio1" />
          <label class="form-check-label" for="sexRatio1">Мужской</label>
        </div>
        <div class="form-check">
          <input class="form-check-input" type="radio" name="flexRadioDefault" id="sexRatio2" />
          <label class="form-check-label" for="sexRatio2">Женский</label>
        </div>
      </div>

      <b className={styles.b}>Возраст</b>
      <Form>
        <Form.Group as={Row} className="mb-3" controlId="minAge">
          <Form.Label column sm="2">
            Min:
          </Form.Label>
          <Col sm="10">
            <Form.Control type="number" defaultValue="18" />
          </Col>
        </Form.Group>

        <Form.Group as={Row} className="mb-3" controlId="maxAge">
          <Form.Label column sm="2">
            Max:
          </Form.Label>
          <Col sm="10">
            <Form.Control type="number" defaultValue="99" />
          </Col>
        </Form.Group>
      </Form>

      <div className={styles.place}>
        <b className={styles.b}>Место</b>
        <div className={styles.placeFields}>
          <Form>
            <Form.Group className="mb-3">
              <Form.Control type="text" placeholder="Страна" id="country" />
              <Form.Control type="text" placeholder="Регион" id="region" />
              <Form.Control type="text" placeholder="Город" id="city" />
            </Form.Group>
          </Form>
        </div>
      </div>

      <b className={styles.b}>Зарплата (в рублях)</b>
      <Form>
        <Form.Group as={Row} className="mb-3" controlId="minSalary">
          <Form.Label column sm="2">
            Min:
          </Form.Label>
          <Col sm="10">
            <Form.Control type="number" defaultValue="100" />
          </Col>
        </Form.Group>

        <Form.Group as={Row} className="mb-3" controlId="maxSalary">
          <Form.Label column sm="2">
            Max:
          </Form.Label>
          <Col sm="10">
            <Form.Control type="number" defaultValue="999999" />
          </Col>
        </Form.Group>
      </Form>

      <div className={styles.place}>
        <b className={styles.b}>Специальности</b>
        <div className={styles.specialitiesField}>
          <StyleOutlineTypetextClea
            label="Рэкетирство "
            styleOutlineTypetextCleaBorder="1px solid var(--color-steelblue-100)"
          />
        </div>
      </div>
      <div className={styles.place}>
        <b className={styles.b}>Умения</b>
        <div className={styles.specialitiesField1}>
          <StyleOutlineTypetextClea
            label="Писать "
            styleOutlineTypetextCleaBorder="1px solid var(--color-steelblue-100)"
          />
          <StyleOutlineTypetextClea
            label="Считать"
            styleOutlineTypetextCleaBorder="1px solid var(--color-steelblue-100)"
          />
          <StyleOutlineTypetextClea
            label="Боксировать"
            styleOutlineTypetextCleaBorder="1px solid var(--color-steelblue-100)"
          />
        </div>
      </div>

      <Form>
        <Form.Group className="mb-3" controlId="submit">
          <Form.Control type="button" defaultValue="Начать поиск" onClick={onSubmitClick} />
        </Form.Group>
      </Form>
    </div>
  );
};

export default FiltersBlock;
