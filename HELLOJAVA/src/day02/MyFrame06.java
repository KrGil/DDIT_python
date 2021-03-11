package day02;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MyFrame06 extends JFrame {

	private JPanel contentPane;
	private JTextField tf_dan;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyFrame06 frame = new MyFrame06();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MyFrame06() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JTextArea ta = new JTextArea();
		ta.setBounds(0, 0, 229, 251);
		contentPane.add(ta);
		
		tf_dan = new JTextField();
		tf_dan.setBounds(238, 2, 97, 21);
		contentPane.add(tf_dan);
		tf_dan.setColumns(10);
		
		JButton btn = new JButton("출력");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				int dan = Integer.parseInt(tf_dan.getText());
				String result = "";
//				for(int j=dan; j < 10; j++) {
//					result += dan+" * "+ j + " = "+ dan*j +"\n";
//					
//				}
//					result += dan+" * "+ j + " = "+ dan*j +"\n";
				String txt = "";
				txt += dan+" * 1 = "+ (dan*1) +"\n";
				txt += dan+" * 2 = "+ (dan*2) +"\n";
				txt += dan+" * 3 = "+ (dan*3) +"\n";
				txt += dan+" * 4 = "+ (dan*4) +"\n";
				txt += dan+" * 5 = "+ (dan*5) +"\n";
				txt += dan+" * 6 = "+ (dan*6) +"\n";
				txt += dan+" * 7 = "+ (dan*7) +"\n";
				txt += dan+" * 8 = "+ (dan*8) +"\n";
				txt += dan+" * 9 = "+ (dan*9) +"\n";
				ta.setText(txt);
			}
		});
		btn.setBounds(238, 33, 97, 23);
		contentPane.add(btn);
	}

}
