import {Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {Observable} from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import {API_URL} from '../env';

@Injectable()
export class ProgressCheckApiService {

  constructor(private http: HttpClient) {
  }

  private static _handleError(err: HttpErrorResponse | any) {
    return Observable.throw(err.message || 'Error: Unable to complete request.');
  }

  // GET list of students and courses
  getStudents(): {
    return this.http
      .get(`${API_URL}/`)
      .catch(ProgressCheckApiService._handleError);
  }
}
