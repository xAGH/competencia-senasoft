import { TestBed } from '@angular/core/testing';

import { LobbyResolver } from './lobby.resolver';

describe('LobbyResolver', () => {
  let resolver: LobbyResolver;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    resolver = TestBed.inject(LobbyResolver);
  });

  it('should be created', () => {
    expect(resolver).toBeTruthy();
  });
});
