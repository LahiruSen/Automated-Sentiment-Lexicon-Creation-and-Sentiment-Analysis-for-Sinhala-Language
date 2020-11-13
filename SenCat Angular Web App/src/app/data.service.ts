import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from '../environments/environment';

export interface ResponseData {
  statusCode: number;
  headers: any;
  body: any;
}

@Injectable({
  providedIn: 'root'
})
export class DataService {

  constructor(private httpClient: HttpClient) { }

  getSentiment(text: string, suffix: string) {
    return this.httpClient.post<ResponseData>(
      'https://q2w8xgcvmk.execute-api.us-east-1.amazonaws.com/dev/' + suffix,
      { text },
      { headers: new HttpHeaders({
          'x-api-key': environment.apiKey
        })}
    );
  }

  getSentiments(text: string) {
    return this.httpClient.post<ResponseData>(
      'https://q2w8xgcvmk.execute-api.us-east-1.amazonaws.com/dev/helasentilex/',
      { text },
      { headers: new HttpHeaders({
          'x-api-key': environment.apiKey
      })}
    );
  }
}
