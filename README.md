# Fair Bidding Scheme

This is an implementation of a private bidding scheme using zkSNARKs and ZoKrates, developed during the ZKP Workshop held in London on June 17th-21st, 2019.

Note: it is a testing and unstable implementation with hardcoded inputs.

## Usage

### Verifier

The verifier needs to compile the ZoKrates code, perform the setup phase and extract the verifier. Then, it sends the necessary files to the prover (this process has been simulated locally) and starts to listen to a specific port for incoming requests (which can be manually verified using the Remix IDE or similar). To perform all these actions, simply run:

```
cd verifier
python verifier.py
```

### Prover

The prover computes the witness, generates the proof and sends it to a verifier server. Simply run:

```
cd prover
python prover.py
```

## Authors

* Konstantinos Karoudis
* Patrick Osborne
* Xavier Salleras
* Karen Scarbrough


