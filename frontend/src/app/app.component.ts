import {Component, OnInit, OnDestroy} from '@angular/core';
import {Subscription} from 'rxjs';
import {ProgressCheckApiService} from './progess_check/progress_check_api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent implements OnInit, OnDestroy {
  title = 'app';
  listSubs: Subscription|undefined;
  examsList: []|undefined;

  constructor(private progressCheckApi: ProgressCheckApiService) {
  }

  ngOnInit() {
    this.listSubs = this.progressCheckApi
      .getStudents()
      .subscribe(res => {
          this.examsList = res;
        },
        console.error
      );
  }

  ngOnDestroy() {
    this.listSubs.unsubscribe();
  }
}
