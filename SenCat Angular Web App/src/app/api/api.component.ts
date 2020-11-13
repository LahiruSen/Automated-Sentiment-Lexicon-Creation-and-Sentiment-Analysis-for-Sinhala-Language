import { Component, OnInit } from '@angular/core';
import { DataService, ResponseData } from '../data.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-api',
  templateUrl: './api.component.html',
  styleUrls: ['./api.component.css']
})
export class ApiComponent implements OnInit {
  text: string;
  suffix: string;
  sentiment: {positive: number, negative: number, neutral?: number, conflict?: number};
  sentiments = {};
  isLoading = false;
  isError = false;

  constructor(private dataService: DataService,
              private route: ActivatedRoute) { }

  ngOnInit(): void {
    if (this.route.snapshot.queryParams.model) {
      this.suffix = this.route.snapshot.queryParams.model;
    } else {
      this.suffix = '';
    }

  }

  onFindSentiment(text: string) {
    this.sentiment = null;
    this.sentiments = null;
    this.text = text;
    this.isLoading = true;
    this.isError = false;

    this.dataService.getSentiment(text, this.suffix).subscribe(response => {
      console.log(response);
      this.sentiment = JSON.parse(response.body);
      this.isLoading = false;
    }, error => {
      console.log(error);
      this.isLoading = false;
      this.isError = true;
    });

    this.dataService.getSentiments(text).subscribe(response => {
      console.log(response);
      this.sentiments = response.body;
    }, error => {
      console.log(error);
      this.isLoading = false;
      this.isError = true;
    });
  }
}
