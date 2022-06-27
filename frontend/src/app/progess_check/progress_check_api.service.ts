import {Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {Observable} from 'rxjs';
import { throwError } from 'rxjs';

import { catchError } from 'rxjs/operators';
import {API_URL} from '../env';

@Injectable()
export class ProgressCheckApiService {

  constructor(private http: HttpClient) {
  }

  private static _handleError(err: HttpErrorResponse | any) {
    return throwError(err.message || 'Error: Unable to complete request.');
  }

  // GET list of students and courses
  getStudents(): Observable<any> {
    return this.http
      .get(`${API_URL}/`)
  }
}
